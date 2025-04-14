import { createFeatureSelector } from '@ngrx/store';

import { videosFeatureKey, VideosState } from '../models/videos-state.model';

export const videosStateFeatureSelector =
  createFeatureSelector<VideosState>(videosFeatureKey);
