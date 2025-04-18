import { HttpErrorResponse } from '@angular/common/http';

import { createAction, props } from '@ngrx/store';

import { VideoApiResponseModel } from '@frontend/video-data';

enum VideosActionNamesEnum {
  LoadVideos = '[Videos] Load Videos',
  LoadVideosSuccess = '[Videos] Load Videos Success',
  LoadVideosError = '[Videos] Load Videos Error',
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
