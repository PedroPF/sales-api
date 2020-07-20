import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public chosenTab = 'Agents';

  constructor() { 
  }

  ngOnInit() {
  }

  onClick(tabName: string){
    this.chosenTab = tabName
    return false
  }
}
