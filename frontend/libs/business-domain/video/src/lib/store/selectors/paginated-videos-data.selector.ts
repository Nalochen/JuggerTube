import { createSelector } from '@ngrx/store';

import { VideosState, VideosStateAware } from '../models/videos-state.model';
import { videosStateFeatureSelector } from './videos-state-feature.selector';
import { VideoApiResponseModel } from '@frontend/video-data';

export const allVideosDataSelector = createSelector<
  VideosStateAware,
  [VideosState],
  VideoApiResponseModel[]
>(videosStateFeatureSelector, (state: VideosState) => state.videos);

export const currentPageSelector = createSelector<
  VideosStateAware,
  [VideosState],
  { start: number; limit: number }
>(videosStateFeatureSelector, (state: VideosState) => ({
  start: state.currentPage.start,
  limit: state.currentPage.limit
}));

export const paginatedVideosDataSelector = createSelector(
  allVideosDataSelector,
  currentPageSelector,
  (videos: VideoApiResponseModel[], page: { start: number; limit: number }) => {
    // Wenn keine Videos vorhanden sind, leeres Array zurückgeben
    if (!videos || videos.length === 0) {
      return [];
    }

    // Stelle sicher, dass wir nicht über das Array hinaus gehen
    const endIndex = Math.min(page.start + page.limit, videos.length);

    // Wenn der Startindex gültig ist, gib die entsprechende Teilmenge zurück
    if (page.start >= 0 && page.start < videos.length) {
      return videos.slice(page.start, endIndex);
    }

    // Fallback: Gib leeres Array zurück, wenn der Index ungültig ist
    return [];
  }
);
