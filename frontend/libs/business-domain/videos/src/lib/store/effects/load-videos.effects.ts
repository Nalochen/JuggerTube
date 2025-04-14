import { HttpErrorResponse } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';
import { catchError, exhaustMap, map } from 'rxjs/operators';

import { Actions, createEffect, ofType } from '@ngrx/effects';
import { Action } from '@ngrx/store';

import {
  loadVideosAction,
  loadVideosActionError,
  loadVideosActionSuccess,
} from '../actions/videos.actions';
import {
  VideoApiResponseModel,
  VideosApiClient,
} from '@frontend/data-domain-videos';

const unknownError = { form: 'Unknown error' };

@Injectable()
export class LoadVideosEffects {
  private readonly actions$ = inject(Actions);
  private readonly videosApiClient = inject(VideosApiClient);

  public readonly loadVideos: Observable<Action> = createEffect(() =>
    this.actions$.pipe(
      ofType(loadVideosAction),
      exhaustMap(() =>
        this.videosApiClient.get().pipe(
          map((videos: VideoApiResponseModel[]) => {
            return loadVideosActionSuccess({
              videos: videos,
            });
          }),
          catchError((response: HttpErrorResponse) => {
            return of(
              loadVideosActionError({
                error: response.status === 422 ? response.error : unknownError,
              })
            );
          })
        )
      )
    )
  );
}
