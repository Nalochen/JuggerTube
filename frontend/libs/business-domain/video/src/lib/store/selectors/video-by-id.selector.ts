import { createSelector } from '@ngrx/store';

import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';
import { VideoApiResponseModel } from '@frontend/video-data';

export const selectVideoById = (videoId: number) =>
  createSelector<VideosStateAware, [VideosState], VideoApiResponseModel | undefined>(
    videosStateFeatureSelector,
    (state: VideosState) => {
      const entries = Object.entries(state.allVideos);
      const found = entries.find(([, video]) => video.id === videoId);
      return found ? found[1] : undefined;
    }
  );
