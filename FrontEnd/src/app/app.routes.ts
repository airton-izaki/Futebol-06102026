import { Routes }       from '@angular/router';
import { Home }         from './page/home/home';
import { Tabela }       from './page/tabela/tabela';
import { ClubeLista }   from './features/clubes/components/clube-lista/clube-lista';
import { Jogos }        from './features/jogos/components/jogos/jogos';
export const routes: Routes = [
  {
    path: '',
    component: Home
  },
  {
    path: 'tabela',
    component: Tabela
  },
  {
    path: 'clubes',
    component: ClubeLista
  },
  {
    path: 'jogos',
    component: Jogos
  },
];
