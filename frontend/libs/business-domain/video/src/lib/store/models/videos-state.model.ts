import { HttpErrorResponse } from '@angular/common/http';

import { RequestStateEnum } from '@frontend/api';
import { VideoApiResponseModel } from '@frontend/video-data';

export const videosFeatureKey = 'videoOverview';

export interface CurrentPage {
  start: number;
  limit: number;
}

export interface VideosState {
  videos: VideoApiResponseModel[];
  requestState: RequestStateEnum;
  error: HttpErrorResponse | null;
  count: number;
  currentPage: CurrentPage;
}

export interface VideosStateAware {
  [videosFeatureKey]: VideosState;
}
