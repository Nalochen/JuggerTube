import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

import { HeaderBarComponent } from './header-bar/header-bar.component';

@Component({
  selector: 'app-root',
  imports: [RouterModule, HeaderBarComponent],
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.less',
})
export class AppComponent {}
