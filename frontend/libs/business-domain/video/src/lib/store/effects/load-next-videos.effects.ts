import { HttpErrorResponse } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';
import { catchError, exhaustMap, map } from 'rxjs/operators';

import { Actions, createEffect, ofType } from '@ngrx/effects';
import { Action } from '@ngrx/store';

import {
  loadNextVideos,
  loadNextVideosError,
  loadNextVideosSuccess,
} from '../actions/videos.actions';
import {PaginatedVideosApiResponseModel, VideosApiClient, VideoApiResponseModel} from '@frontend/video-data';

const unknownError = { form: 'Unknown error' };

function convertStringToDate(dateStr: string): Date {
  if (!dateStr) return new Date();
  const [day, month, year] = dateStr.split('-').map(num => parseInt(num, 10));
  return new Date(year, month - 1, day);
}

function convertDatesInVideo(video: VideoApiResponseModel): VideoApiResponseModel {
  return {
    ...video,
    uploadDate: convertStringToDate(video.uploadDate as unknown as string),
    dateOfRecording: convertStringToDate(video.dateOfRecording as unknown as string)
  };
}

@Injectable()
export class LoadNextVideosEffects {
  private readonly actions$ = inject(Actions);
  private readonly videosApiClient = inject(VideosApiClient);

  public readonly loadNextVideos: Observable<Action> = createEffect(() =>
    this.actions$.pipe(
      ofType(loadNextVideos),
      exhaustMap((action: ReturnType<typeof loadNextVideos>) =>
        this.videosApiClient.getPaginatedVideos(action.start, action.limit).pipe(
          map((data: PaginatedVideosApiResponseModel) => {
            const convertedVideos = data.results.map(convertDatesInVideo);
            return loadNextVideosSuccess({
              videos: convertedVideos,
              count: data.count,
              previous: data.previous,
              next: data.next,
            });
          }),
          catchError((response: HttpErrorResponse) => {
            return of(
              loadNextVideosError({
                error: response.status === 422 ? response.error : unknownError,
              })
            );
          })
        )
      )
    )
  );
}
