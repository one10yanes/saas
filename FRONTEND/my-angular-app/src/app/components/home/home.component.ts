import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  data: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.apiService.getData().subscribe(response => {
      this.data = response;
    });
  }

  handleUserInteraction(): void {
    // Logic for handling user interactions
  }
}