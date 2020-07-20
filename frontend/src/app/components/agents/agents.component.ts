import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-agents',
  templateUrl: './agents.component.html',
  styleUrls: ['./agents.component.css']
})
export class AgentsComponent implements OnInit {
  public isCollapsed = true;
  public newAgentForm;

  public agents: any = [];

  constructor(private formBuilder: FormBuilder, private http: HttpClient) { 
    this.newAgentForm = this.formBuilder.group({
      name: '',
      city: '',
      birthday: '',
      hire_date: '',
    });

    this.updateAgents();
  }

  updateAgents(){
    this.http.get('/agent/').subscribe( msg => {
      this.agents = msg;
    })
  }

  insertAgent(value){
    const newAgent = {
      name: value['name'],
      city: value['city'],
      birthday: `${value['birthday']['year']}-${value['birthday']['month']}-${value['birthday']['day']}`,
      hire_date: `${value['hire_date']['year']}-${value['hire_date']['month']}-${value['hire_date']['day']}`,
    }
    this.http.post('/agent/', newAgent).subscribe(() => console.log('ok'));
  }

  ngOnInit() {
  }

  onSubmit(value){
    console.log(value);
    this.newAgentForm = this.formBuilder.group({
      name: '',
      city: '',
      birthday: '',
      hire_date: '',
    })
    this.insertAgent(value)
    this.updateAgents();
    return false;
  }
}
