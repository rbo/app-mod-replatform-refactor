package com.lemberski.serviceb;

import static java.util.Collections.singletonMap;

import java.util.Map;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/service-b")
public class ServiceResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Map<String, String> hello() {
        return singletonMap("messsage", "Hello from NEW service b");
    }

}
