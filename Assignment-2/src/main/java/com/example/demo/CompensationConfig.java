package com.example.demo;

import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.ElasticsearchTransport;
import co.elastic.clients.transport.rest_client.RestClientTransport;
import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.elasticsearch.client.RestClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.net.ssl.SSLContext;

import static com.example.demo.Constants.*;

@Configuration
public class CompensationConfig {
    @Bean
    public RestClient getRestClient() {
        SSLContext sslContext = TransportUtil
                .sslContextFromCaFingerprint(FINGERPRINT);

        BasicCredentialsProvider credsProv = new BasicCredentialsProvider();
        credsProv.setCredentials(
                AuthScope.ANY, new UsernamePasswordCredentials(LOGIN, PASSWORD)
        );
        RestClient restClient = RestClient
                .builder(HttpHost.create(SERVERUrl))
                .setHttpClientConfigCallback(hc -> hc
                        .setSSLContext(sslContext)
                        .setDefaultCredentialsProvider(credsProv)
                ).build();
        return restClient;
    }

    @Bean
    public ElasticsearchTransport getElasticsearchTransport() {
        return new RestClientTransport(getRestClient(), new JacksonJsonpMapper());
    }

    @Bean
    public ElasticsearchClient getElasticsearchClient() {
        ElasticsearchClient elasticsearchClient = new ElasticsearchClient(getElasticsearchTransport());
        return elasticsearchClient;
    }
}

