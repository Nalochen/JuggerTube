import { HttpErrorResponse } from '@angular/common/http';

import { createAction, props } from '@ngrx/store';

import { VideoApiResponseModel } from '@frontend/video-data';

enum VideosActionNamesEnum {
  LoadVideos = '[Videos] Load Videos',
  LoadVideosSuccess = '[Videos] Load Videos Success',
  LoadVideosError = '[Videos] Load Videos Error',
  LoadPaginatedVideos = '[Videos] Load Paginated Videos',
  LoadPaginatedVideosSuccess = '[Videos] Load Paginated Videos Success',
  LoadPaginatedVideosError = '[Videos] Load Paginated Videos Error',
  LoadNextVideos = '[Videos] Load Next Videos',
  LoadNextVideosSuccess = '[Videos] Load Next Videos Success',
  LoadNextVideosError = '[Videos] Load Next Videos Error',
}

export const loadVideosAction = createAction(VideosActionNamesEnum.LoadVideos);

export const loadVideosActionSuccess = createAction(
  VideosActionNamesEnum.LoadVideosSuccess,
  props<{
    videos: VideoApiResponseModel[];
  }>()
);

export const loadVideosActionError = createAction(
  VideosActionNamesEnum.LoadVideosError,
  props<{
    error: HttpErrorResponse;
  }>()
);

export const loadPaginatedVideosAction = createAction(
  VideosActionNamesEnum.LoadPaginatedVideos,
  props<{
    start: number;
    limit: number;
  }>()
);

export const loadPaginatedVideosActionSuccess = createAction(
  VideosActionNamesEnum.LoadPaginatedVideosSuccess,
  props<{
    videos: VideoApiResponseModel[];
    count: number;
    previous: string | null;
    next: string | null;
  }>()
);

export const loadPaginatedVideosActionError = createAction(
  VideosActionNamesEnum.LoadPaginatedVideosError,
  props<{
    error: HttpErrorResponse;
  }>()
);

export const loadNextVideos = createAction(
  VideosActionNamesEnum.LoadNextVideos,
  props<{
    start: number;
    limit: number;
  }>()
);

export const loadNextVideosSuccess = createAction(
  VideosActionNamesEnum.LoadNextVideosSuccess,
  props<{
    videos: VideoApiResponseModel[];
    count: number;
    previous: string | null;
    next: string | null;
  }>()
);

export const loadNextVideosError = createAction(
  VideosActionNamesEnum.LoadNextVideosError,
  props<{
    error: HttpErrorResponse;
  }>()
);
