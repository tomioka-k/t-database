from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router, Query
from config import auth

from ..models.video import Video, Tag, Category

from ..schemas.videos import CategorySchema, VideoSchema, TagSchema, VideoFilters

router = Router(auth=auth.header_key)


@router.get("/", response=List[VideoSchema])
def read_videos(request, filters: VideoFilters = Query(...)):
    qs = Video.objects.filter(
       
    )[filters.offset:filters.limit]
    return qs

@router.get("/tags", response=List[TagSchema])
def read_tags(request):
    qs = Tag.objects.all()
    return qs

@router.get("/categoies", response=List[CategorySchema])
def read_categories(request):
    qs = Category.objects.all()
    return qs

@router.get("/{video_id}", response=VideoSchema)
def read_video(request, video_id: int):
    qs = get_object_or_404(Video, id=video_id)
    return qs
