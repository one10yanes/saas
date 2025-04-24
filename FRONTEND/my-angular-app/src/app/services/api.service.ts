export class ApiService {
    private baseUrl: string = 'http://localhost:5000/api'; // Adjust the base URL as needed

    constructor(private http: HttpClient) {}

    getData(endpoint: string): Observable<any> {
        return this.http.get(`${this.baseUrl}/${endpoint}`);
    }

    postData(endpoint: string, data: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/${endpoint}`, data);
    }
}