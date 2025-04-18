import {
  provideHttpClient,
  withInterceptorsFromDi,
} from '@angular/common/http';
import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { provideRouter } from '@angular/router';

import { provideEffects } from '@ngrx/effects';
import { provideStore } from '@ngrx/store';

import {
  metaReducers,
  reducers,
} from '../../../../libs/business-domain/video/src/lib/store/reducers';
import { appRoutes } from './app.routes';
import { LoadVideosEffects } from '@frontend/video';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(appRoutes),
    provideAnimationsAsync(),
    provideStore(reducers, { metaReducers }),
    provideEffects([LoadVideosEffects]),
    provideHttpClient(withInterceptorsFromDi()),
  ],
};
