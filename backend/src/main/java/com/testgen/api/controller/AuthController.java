package com.testgen.api.controller;
import com.testgen.api.service.AuthService; import jakarta.validation.constraints.*; import org.springframework.web.bind.annotation.*; import java.util.*;
@RestController @RequestMapping("/api/auth") @CrossOrigin(origins="*") public class AuthController { private final AuthService auth; public AuthController(AuthService a){auth=a;}
 public record Register(@NotBlank String name,@Email String email,@Size(min=8) String password){} public record Login(@Email String email,@NotBlank String password){}
 @PostMapping("/register") public Map<String,String> register(@RequestBody Register r){return Map.of("token",auth.register(r.name(),r.email(),r.password()));}
 @PostMapping("/login") public Map<String,String> login(@RequestBody Login r){return Map.of("token",auth.login(r.email(),r.password()));}
 @PostMapping("/forgot-password") public Map<String,String> forgot(){return Map.of("message","Password reset workflow placeholder; connect email provider in production.");}
}
