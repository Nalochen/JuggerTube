import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DataDomainVideosComponent } from '@frontend/data-domain-videos';

describe('DataDomainVideosComponent', () => {
  let component: DataDomainVideosComponent;
  let fixture: ComponentFixture<DataDomainVideosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DataDomainVideosComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(DataDomainVideosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
