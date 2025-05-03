import { createSelector } from '@ngrx/store';

import { getVideosFromDict } from '../../utils/range-utils';
import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';
import { VideoApiResponseModel } from '@frontend/video-data';

export const paginatedVideosDataSelector = createSelector<
  VideosStateAware,
  [VideosState],
  VideoApiResponseModel[]
>(videosStateFeatureSelector, (state: VideosState) => {
  return getVideosFromDict(state.allVideos, state.currentView.displayedVideos);
});
