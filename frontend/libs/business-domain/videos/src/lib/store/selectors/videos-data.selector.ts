import { createSelector } from '@ngrx/store';

import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';
import { VideoApiResponseModel } from '@frontend/data-domain-videos';

export const videosDataSelector = createSelector<
  VideosStateAware,
  [VideosState],
  VideoApiResponseModel[]
>(videosStateFeatureSelector, (state: VideosState) => state.videos);
