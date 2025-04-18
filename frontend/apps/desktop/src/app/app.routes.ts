import { Route } from '@angular/router';

import { PageCreateVideoComponent } from './pages/page-create-video/page-create-video.component';
import { PageLoginComponent } from './pages/page-login/page-login.component';
import { PageRegisterComponent } from './pages/page-register/page-register.component';
import { PageUserDetailsComponent } from './pages/page-user-details/page-user-details.component';
import { PageVideoDetailsComponent } from './pages/page-video-details/page-video-details.component';
import { PageVideoOverviewComponent } from './pages/page-video-overview/page-video-overview.component';

export const appRoutes: Route[] = [
  {
    path: 'video-overview',
    component: PageVideoOverviewComponent,
  },
  {
    path: 'video-details/:id',
    component: PageVideoDetailsComponent,
  },
  {
    path: 'create-video',
    component: PageCreateVideoComponent,
  },
  {
    path: 'user-details',
    component: PageUserDetailsComponent,
  },
  {
    path: 'register',
    component: PageRegisterComponent,
  },
  {
    path: 'login',
    component: PageLoginComponent,
  },
  {
    path: '**',
    redirectTo: 'video-overview',
  },
];
