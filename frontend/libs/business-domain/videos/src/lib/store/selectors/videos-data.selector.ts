import {createSelector} from "@ngrx/store";
import {VideosState, VideosStateAware} from "../models/videos-state.model";
import {VideoApiResponseModel} from "@frontend/data-domain-videos";
import {videosStateFeatureSelector} from "./videos-state-feature.selector";

export const videosDataSelector = createSelector<
  VideosStateAware,
  [VideosState],
  VideoApiResponseModel[]
>(
  videosStateFeatureSelector,
  (state: VideosState) => state.videos,
);
