import {Injectable} from "@angular/core";
import {Actions, createEffect, ofType} from "@ngrx/effects";
import {VideoApiResponseModel, VideosApiClient} from "@frontend/data-domain-videos";
import {Observable, of} from "rxjs";
import {Action} from "@ngrx/store";
import {loadVideosAction, loadVideosActionError, loadVideosActionSuccess} from "../actions/videos.actions";
import { catchError, exhaustMap, map } from 'rxjs/operators';
import {HttpErrorResponse} from "@angular/common/http";

const unknownError = { form: 'Unknown error' };

@Injectable()
export class LoadVideosEffects {
  constructor(
    private readonly actions$: Actions,
    private readonly videosApiClient: VideosApiClient
  ) {}

  public readonly loadVideos: Observable<Action> = createEffect(() =>
    this.actions$.pipe(
      ofType(loadVideosAction),
      exhaustMap((action: ReturnType<typeof loadVideosAction>) =>
        this.videosApiClient
          .get()
          .pipe(
            map((videos: VideoApiResponseModel[]) => {
              return loadVideosActionSuccess({
                videos: videos
              });
            }),
            catchError((response: HttpErrorResponse) =>
              of(
                loadVideosActionError({
                  error:
                    response.status === 422
                      ? response.error
                      : unknownError,
                })
              )
            )
          )
      )
    )
  );
}
