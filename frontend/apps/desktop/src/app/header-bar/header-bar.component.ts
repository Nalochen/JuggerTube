import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'header-bar',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './header-bar.component.html',
  styleUrl: './header-bar.component.less',
})
export class HeaderBarComponent {}
