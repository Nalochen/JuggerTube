import {
  provideHttpClient,
  withInterceptorsFromDi,
} from '@angular/common/http';
import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { provideEffects } from '@ngrx/effects';
import { provideStore } from '@ngrx/store';

import {
  metaReducers,
  reducers,
} from '../../../../libs/business-domain/videos/src/lib/store/reducers';
import { appRoutes } from './app.routes';
import { LoadVideosEffects } from '@frontend/business-domain-videos';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(appRoutes),
    provideStore(reducers, { metaReducers }),
    provideEffects([LoadVideosEffects]),
    provideHttpClient(withInterceptorsFromDi()),
  ],
};
