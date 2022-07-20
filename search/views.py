from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics, status
from .models import Paragraph
from .serializers import ParagraphSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import re
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


# for url with no inputs i.e list and create
class ParagraphView(generics.GenericAPIView):
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    # funtion name has to be that of the method it uses
    @swagger_auto_schema(operation_summary="List all paragraphs")
    def get(self, request: Request):
        paras = Paragraph.objects.all()
        serializer = self.serializer_class(instance=paras, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create new paragraphs")
    def post(self, request: Request):
        data = request.data
        str1 = str(data["paragraph"]).split("\n\n")
        for s in str1:
            paragraphs = {
                "paragraph": s.lower(),
                "author": request.user.id,
            }
            serializer = self.serializer_class(data=paragraphs)

            if serializer.is_valid():
                serializer.save()
                response = {"message": "Paragraph Created", "data": serializer.data}

        return Response(data=response, status=status.HTTP_201_CREATED)


# for deleting paragraphs
class ParagraphDelete(APIView):
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Show paragraph by id")
    def get(self, request: Request, paragraph_id):
        paragraph = get_object_or_404(Paragraph, id=paragraph_id)
        serializer = self.serializer_class(instance=paragraph)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # delete paragraph individually
    @swagger_auto_schema(operation_summary="Delete paragraph by id")
    def delete(self, request: Request, paragraph_id):
        paragraph = get_object_or_404(Paragraph, id=paragraph_id)
        paragraph.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# for searching word in all paragraphs in db.
class ParagraphSreach(APIView):
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    # returns list of all paragraphs in db.
    data = Paragraph.objects.values_list("paragraph", flat=True)

    @swagger_auto_schema(operation_summary="Search paragraphs containing the word")
    def get(self, request: Request, word):
        paragraphs = self.data
        paragraph_present = []

        for paragraph in paragraphs:
            if findWholeWord(word)(paragraph):
                paragraph_present.append(paragraph)

        response = {
            "paragraphs with word present": paragraph_present[:10],
            "count": len(paragraph_present[:10]),
        }
        # print(paragraph_present)
        return Response(data=response, status=status.HTTP_200_OK)


# to find whole word in paragraph
def findWholeWord(w):
    return re.compile(r"\b({0})\b".format(w), flags=re.IGNORECASE).search
