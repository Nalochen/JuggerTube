import { createReducer, on } from '@ngrx/store';

import {
  loadNextVideos, loadNextVideosError, loadNextVideosSuccess,
  loadPaginatedVideosAction, loadPaginatedVideosActionError, loadPaginatedVideosActionSuccess,
  loadVideosAction,
  loadVideosActionError,
  loadVideosActionSuccess,
} from '../actions/videos.actions';
import { VideosState } from '../models/videos-state.model';
import { RequestStateEnum } from '@frontend/api';
import { VideoApiResponseModel } from '@frontend/video-data';

export const initialState: VideosState = {
  videos: [],
  requestState: RequestStateEnum.Initial,
  count: 0,
  error: null,
  currentPage: {
    start: 1,
    limit: 20
  }
};

function mergeVideos(existingVideos: VideoApiResponseModel[], newVideos: VideoApiResponseModel[], startIndex: number): VideoApiResponseModel[] {
  // Erstelle eine Kopie des existierenden Arrays
  const result = [...existingVideos];
  
  // Fülle das Array mit den neuen Videos an den richtigen Positionen
  for (let i = 0; i < newVideos.length; i++) {
    result[startIndex - 1 + i] = newVideos[i];
  }
  
  // Entferne undefined Einträge und gib das Array zurück
  return result.filter(video => video !== undefined);
}

export const videosReducer = createReducer(
  initialState,
  on(loadVideosAction, (state: VideosState): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  }),
  on(loadVideosActionSuccess, (state: VideosState, action): VideosState => {
    return {
      ...state,
      videos: action.videos,
      requestState: RequestStateEnum.Success,
    };
  }),
  on(loadVideosActionError, (state: VideosState, { error }): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Error,
      error: error,
    };
  }),
  on(loadPaginatedVideosAction, (state: VideosState, { start, limit }): VideosState => {
    return {
      ...state,
      currentPage: { start, limit },
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  }),
  on(loadPaginatedVideosActionSuccess, (state: VideosState, action): VideosState => {
    return {
      ...state,
      videos: action.videos,
      count: action.count,
      requestState: RequestStateEnum.Success,
    };
  }),
  on(loadPaginatedVideosActionError, (state: VideosState, { error }): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Error,
      error: error,
    };
  }),
  on(loadNextVideos, (state: VideosState, { start, limit }): VideosState => {
    return {
      ...state,
      currentPage: { start, limit },
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  }),
  on(loadNextVideosSuccess, (state: VideosState, action): VideosState => {
    return {
      ...state,
      videos: mergeVideos(state.videos, action.videos, state.currentPage.start),
      count: action.count,
      requestState: RequestStateEnum.Success,
    };
  }),
  on(loadNextVideosError, (state: VideosState, { error }): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Error,
      error: error,
    };
  })
);
