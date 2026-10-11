import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubeLista } from './clube-lista';

describe('ClubeLista', () => {
  let component: ClubeLista;
  let fixture: ComponentFixture<ClubeLista>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClubeLista],
    }).compileComponents();

    fixture = TestBed.createComponent(ClubeLista);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
