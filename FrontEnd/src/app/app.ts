import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MenuItem } from 'primeng/api';
import { MenubarModule } from 'primeng/menubar';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MenubarModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  items: MenuItem[] = [
    {
      label: 'Home',
      icon: 'pi pi-home',
      routerLink: ['/']
    },
    {
      label: 'Tabela',
      icon: 'pi pi-star',
      routerLink: ['/tabela'] },
    {
      label: 'Clube',
        icon: 'pi pi-plus',
        routerLink: ['/clube/listar'],
          items: [
            {
              label: 'Novos Clubes',
              icon: 'pi pi-shield',
              routerLink: ['/clube/cadastrar'],
            }
          ]
    },
    {
      label: 'Jogos',
      icon: 'pi pi-calendar',
      routerLink: ['/jogos']
    }
  ];
}
