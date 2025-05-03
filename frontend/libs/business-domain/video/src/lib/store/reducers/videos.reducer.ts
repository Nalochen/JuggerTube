import { createReducer, on } from '@ngrx/store';

import { getDisplayedVideoIndices,mergeRanges, videosToDict } from '../../utils/range-utils';
import {
  cacheVideos,
  loadNextVideos,
  loadNextVideosError,
  loadNextVideosSuccess,
  loadPaginatedVideosAction,
  loadPaginatedVideosActionError,
  loadPaginatedVideosActionSuccess,
  mergeVideoRanges,
  requestVideoRange,
  updateCurrentView} from '../actions/videos.actions';
import { VideosState } from '../models/videos-state.model';
import { RequestStateEnum } from '@frontend/api';

export const initialState: VideosState = {
  allVideos: {},
  loadedRanges: [],
  requestState: RequestStateEnum.Initial,
  count: 0,
  error: null,
  currentView: {
    start: 0,
    limit: 20,
    displayedVideos: []
  }
};

export const videosReducer = createReducer(
  initialState,
  on(loadPaginatedVideosAction, (state: VideosState, { start, limit }): VideosState => {
    return {
      ...state,
      currentView: {
        start,
        limit,
        displayedVideos: getDisplayedVideoIndices(start, limit)
      },
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  }),
  on(loadPaginatedVideosActionSuccess, (state: VideosState, action): VideosState => {
    const videoDict = videosToDict(action.videos, state.currentView.start);
    const newRange = {
      start: state.currentView.start,
      end: state.currentView.start + action.videos.length - 1
    };

    return {
      ...state,
      allVideos: { ...state.allVideos, ...videoDict },
      loadedRanges: mergeRanges([...state.loadedRanges, newRange]),
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
      currentView: {
        start,
        limit,
        displayedVideos: getDisplayedVideoIndices(start, limit)
      },
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  }),
  on(loadNextVideosSuccess, (state: VideosState, action): VideosState => {
    const videoDict = videosToDict(action.videos, state.currentView.start);
    const newRange = {
      start: state.currentView.start,
      end: state.currentView.start + action.videos.length - 1
    };

    return {
      ...state,
      allVideos: { ...state.allVideos, ...videoDict },
      loadedRanges: mergeRanges([...state.loadedRanges, newRange]),
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
  }),
  on(mergeVideoRanges, (state: VideosState, { ranges }): VideosState => {
    return {
      ...state,
      loadedRanges: mergeRanges(ranges),
    };
  }),
  on(updateCurrentView, (state: VideosState, { start, limit, displayedVideos }): VideosState => {
    return {
      ...state,
      currentView: {
        start,
        limit,
        displayedVideos
      },
    };
  }),
  on(cacheVideos, (state: VideosState, { videos, range }): VideosState => {
    const videoDict = videosToDict(videos, range.start);
    return {
      ...state,
      allVideos: { ...state.allVideos, ...videoDict },
      loadedRanges: mergeRanges([...state.loadedRanges, range]),
    };
  }),
  on(requestVideoRange, (state: VideosState): VideosState => {
    return {
      ...state,
      requestState: RequestStateEnum.Pending,
      error: null,
    };
  })
);
