import { createSelector } from '@ngrx/store';

import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';
import { RequestStateEnum } from '@frontend/api';

export const videosRequestStateSelector = createSelector<
  VideosStateAware,
  [VideosState],
  RequestStateEnum
>(videosStateFeatureSelector, (state: VideosState) => state.requestState);
