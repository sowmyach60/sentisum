package com.example.demo;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/compensation_data")
public class CompensationController {
    @Autowired
    CompensationService compensationService;


    @GetMapping("/filter")
    List<Compensation> filterResults(@RequestParam double salary, @RequestParam String city) {
        return compensationService.filterSalaryAndCity(salary, city);
    }

    @GetMapping("/sort")
    List<Compensation> sortByTimeStampAndSalary() {
        return compensationService.sortByTimeStampAndSalary();
    }


}
