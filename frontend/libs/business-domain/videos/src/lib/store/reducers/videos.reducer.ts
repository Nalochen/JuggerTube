import { VideosState } from '../models/videos-state.model';
import { createReducer, on } from '@ngrx/store';
import {
  loadVideosAction,
  loadVideosActionError,
  loadVideosActionSuccess,
} from '../actions/videos.actions';
import { RequestStateEnum } from '@frontend/api';

export const initialState: VideosState = {
  videos: [],
  requestState: RequestStateEnum.Initial,
};

export const videosReducer = createReducer(
  initialState,
  on(loadVideosAction, (state: VideosState): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Pending,
    };
  }),
  on(
    loadVideosActionSuccess,
    (state: VideosState, action): VideosState => {
      return {
        ...state,
        videos: action.videos,
        requestState: RequestStateEnum.Success,
      };
    }
  ),
  on(
    loadVideosActionError,
    (state: VideosState): VideosState => {
      return {
        ...state,
        requestState: RequestStateEnum.Error,
      };
    }
  )
)
