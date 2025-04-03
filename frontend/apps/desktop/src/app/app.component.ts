import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

import { HeaderBarComponent } from './header-bar/header-bar.component';

export enum TagContent {
  TRAINING = 'training',
  PODCAST = 'podcast',
  HIGHLIGHTS = 'highlights',
}

export interface Channel {
  id: number;
  name: string;
  escapedName: string;
}

export interface Video {
  id: number;
  title: string;
  description: string;
  url: string;
  uploadedAt: string;
  createdAt: string;
  channel: Channel;
  tags: TagContent[];
}

@Component({
  selector: 'app-root',
  imports: [RouterModule, HeaderBarComponent],
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.less',
})
export class AppComponent {}
