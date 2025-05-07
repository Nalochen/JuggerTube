import { createSelector } from '@ngrx/store';

import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';

export const totalCountVideosDataSelector = createSelector<
  VideosStateAware,
  [VideosState],
  number
>(videosStateFeatureSelector, (state: VideosState) => state.count);
