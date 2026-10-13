import { Routes }         from '@angular/router';
import { Home }           from './page/home/home';
import { Tabela }         from './page/tabela/tabela';
import { ClubeCadastro }  from './features/clubes/components/clube-cadastro/clube-cadastro';
import { ClubeLista }     from './features/clubes/components/clube-lista/clube-lista';
import { Jogos }          from './features/jogos/components/jogos/jogos';
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
    path: 'clube/listar',
    component: ClubeLista
  },
  {
    path: 'clube/cadastrar',
    component: ClubeCadastro
  },
  {
    path: 'clubes',
    redirectTo: 'clube/listar',
    pathMatch: 'full'
  },

  {
    path: 'jogos',
    component: Jogos
  },
];
