import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {
  public isCollapsed = true;
  public newReportForm;
  public names: string[] = [];
  public filter: string = '';
  public filtered_reports: any[] = [];
  public reports: any[] = [];

  constructor(private formBuilder: FormBuilder, private http: HttpClient) {
    this.newReportForm = this.formBuilder.group({
      agent_name: '',
      volume: '',
      period: '',
    });
    
    this.updateReports();


    this.http.get<any[]>('/agent/').subscribe(msg => {
      msg.forEach(element => {
        this.names.push(element['name']);
      });
      this.newReportForm.patchValue({ agent_name: this.names[0] });
    });
  }

  updateReports(){
    this.http.get<any[]>('/report/').subscribe( msg => {
      this.reports = msg;
      console.log(this.reports);
      this.filterReports();
    })
  }

  filterReports(){
    if(this.filter == ''){
      this.filtered_reports = this.reports;
      return;
    }
    this.filtered_reports = this.reports.filter( report => report.agent_name == this.filter);
  }

  onFilter(name){
    this.filter = name;
    this.filterReports();
    return false;
  }

  clearFilter(){
    this.filtered_reports = this.reports;
  }

  insertReport(value){
    const newReport = {
      agent_name: value['agent_name'],
      volume: value['volume'],
      period: `${value['period']['year']}, ${value['period']['month']}`
    }
    return this.http.post('/report/', newReport);
  }

  chooseAgent(name) {
    this.newReportForm.agent_name = name;
    return false
  }

  onSubmit(value){
    this.insertReport(value).subscribe( () => {
      this.updateReports();
    });
    return false;
  }

  ngOnInit() {
  }

}
