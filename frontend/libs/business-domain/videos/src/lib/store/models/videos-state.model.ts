import { VideoApiResponseModel } from "../../../../../../data-domain/videos/src";
import { RequestStateEnum } from "@frontend/api";

export const videosFeatureKey = 'videos';

export interface VideosState {
  videos: VideoApiResponseModel[],
  requestState: RequestStateEnum,
}

export interface VideosStateAware {
  [videosFeatureKey]: VideosState;
}
