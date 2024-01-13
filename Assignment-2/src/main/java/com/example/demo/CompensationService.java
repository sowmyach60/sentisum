package com.example.demo;

import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.elasticsearch._types.FieldSort;
import co.elastic.clients.elasticsearch._types.SortOrder;
import co.elastic.clients.elasticsearch._types.query_dsl.MatchQuery;
import co.elastic.clients.elasticsearch._types.query_dsl.Query;
import co.elastic.clients.elasticsearch._types.query_dsl.RangeQuery;
import co.elastic.clients.elasticsearch.core.SearchResponse;
import co.elastic.clients.elasticsearch.core.search.Hit;
import co.elastic.clients.json.JsonData;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

import static com.example.demo.Constants.INDEX;

@Service
public class CompensationService {

    private static final Logger logger = LoggerFactory.getLogger(CompensationService.class);
    @Autowired
    ElasticsearchClient elasticsearchClient;

    /**
     * returns <code>Compensation List</code> Filters city with
     * greater than given @Param salary in specific @Param city
     */
    List<Compensation> filterSalaryAndCity(double salary, String city) {
        try {
            Query byCity = MatchQuery.of(m -> m
                    .field("city")
                    .query(city)
            )._toQuery();

            Query byMaxSalary = RangeQuery.of(r -> r
                    .field("salary")
                    .gte(JsonData.of(salary))
            )._toQuery();

            SearchResponse<Compensation> response = elasticsearchClient.search(s -> s
                            .index(INDEX)
                            .query(q -> q
                                    .bool(b -> b
                                            .must(byCity)
                                            .must(byMaxSalary)
                                    )
                            ),
                    Compensation.class
            );
            return getMatchedCompensations(response);

        } catch (Exception e) {
            logger.error("An error occurred while filtering: {}", e.getMessage(), e);
            return new ArrayList<>();
        }
    }

    /**
     * returns <code>Compensation List</code> sorted by
     * timestamp in desc and salary in asc
     */
    List<Compensation> sortByTimeStampAndSalary() {
        try {
            SearchResponse<Compensation> response = elasticsearchClient.search(s -> s
                            .index("search-compensation-details")
                            .sort(so -> so.field(FieldSort.of(f -> f
                                    .field("timestamp.keyword")
                                    .order(SortOrder.Desc))
                            )).sort(so -> so.field(FieldSort.of(f -> f
                                    .field("salary.keyword")
                                    .order(SortOrder.Desc))
                            ))
                    , Compensation.class);
            return getMatchedCompensations(response);
        } catch (Exception e) {
            logger.error("An error occurred while sorting : {}", e.getMessage(), e);
            return new ArrayList<>();
        }
    }

    List<Compensation> getMatchedCompensations(SearchResponse<Compensation> searchResponse) {
        List<Hit<Compensation>> hits = searchResponse.hits().hits();
        List<Compensation> compensationList = new ArrayList<>();
        for (Hit<Compensation> hit : hits) {
            compensationList.add(hit.source());
        }
        return compensationList;
    }

}
