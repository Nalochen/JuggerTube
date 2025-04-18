import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'header-bar',
  imports: [CommonModule, RouterLink],
  standalone: true,
  templateUrl: './header-bar.component.html',
  styleUrl: './header-bar.component.less',
})
export class HeaderBarComponent {}
