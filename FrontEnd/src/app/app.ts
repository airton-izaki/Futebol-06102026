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
      label: 'Clubes',
      icon: 'pi pi-shield',
      routerLink: ['/clubes']
    },
    {
      label: 'Jogos',
      icon: 'pi pi-calendar',
      routerLink: ['/jogos']
    }
  ];
}
