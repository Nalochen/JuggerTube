import { HttpErrorResponse } from '@angular/common/http';

import { RequestStateEnum } from '@frontend/api';
import { VideoApiResponseModel } from '@frontend/video-data';

export const videosFeatureKey = 'videoOverview';

export interface VideosState {
  videos: VideoApiResponseModel[];
  requestState: RequestStateEnum;
  error: HttpErrorResponse | null;
}

export interface VideosStateAware {
  [videosFeatureKey]: VideosState;
}
