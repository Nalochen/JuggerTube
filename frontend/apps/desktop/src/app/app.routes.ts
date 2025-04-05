import { Route } from '@angular/router';

import { PageVideoOverviewComponent } from './pages/page-video-overview/page-video-overview.component';

export const appRoutes: Route[] = [
  {
    path: 'video-overview',
    component: PageVideoOverviewComponent,
  },
  {
    path: '**',
    redirectTo: 'video-overview',
  },
];
