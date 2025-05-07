import { LoadedRange } from '../store/models/videos-state.model';
import { VideoApiResponseModel } from '@frontend/video-data';

export function mergeRanges(ranges: LoadedRange[]): LoadedRange[] {
  if (ranges.length <= 1) return ranges;
  
  const sortedRanges = [...ranges].sort((a, b) => a.start - b.start);
  const result: LoadedRange[] = [{ ...sortedRanges[0] }];
  
  for (const range of sortedRanges.slice(1)) {
    const last = result[result.length - 1];
    if (range.start <= last.end + 1) {
      result[result.length - 1] = {
        start: last.start,
        end: Math.max(last.end, range.end)
      };
    } else {
      result.push({ ...range });
    }
  }
  
  return result;
}

export function isRangeCached(start: number, limit: number, loadedRanges: LoadedRange[]): boolean {
  return loadedRanges.some(range => 
    start >= range.start && (start + limit - 1) <= range.end
  );
}

export function videosToDict(videos: VideoApiResponseModel[], startIndex: number): { [key: number]: VideoApiResponseModel } {
  return videos.reduce((acc, video, index) => {
    acc[startIndex + index] = video;
    return acc;
  }, {} as { [key: number]: VideoApiResponseModel });
}

export function getDisplayedVideoIndices(start: number, limit: number): number[] {
  return Array.from({ length: limit }, (_, i) => start + i);
}

export function getVideosFromDict(dict: { [key: number]: VideoApiResponseModel }, indices: number[]): VideoApiResponseModel[] {
  return indices
    .map(index => dict[index])
    .filter(video => video !== undefined);
} 