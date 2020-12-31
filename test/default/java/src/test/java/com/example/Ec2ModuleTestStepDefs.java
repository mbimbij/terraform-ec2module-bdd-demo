package com.example;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.*;

import java.nio.file.Paths;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;
import java.util.stream.Collectors;

import static org.assertj.core.api.Assertions.assertThat;

@Slf4j
public class Ec2ModuleTestStepDefs {

  private Ec2Client ec2Client;
  private Region region;
  private String correlationId;
  private String terraformScriptPath = "../../../examples/default";

  @Before
  public void setUp() {
    correlationId = UUID.randomUUID().toString();
    Utils.executeLinuxShellCommand("terraform init", Paths.get(terraformScriptPath));
  }

  @After
  public void tearDown(){
    Utils.executeLinuxShellCommand("terraform destroy -auto-approve", Paths.get(terraformScriptPath));
  }

  @Given("the region {string}")
  public void theRegion(String region) {
    this.region = Region.of(region);
    ec2Client = Ec2Client.builder()
        .region(this.region)
        .build();
  }

  @Given("an account with only the default VPC")
  public void anAccountWithOnlyTheDefaultVPC() {
    DescribeVpcsResponse describeVpcsResponse = ec2Client.describeVpcs();
    assertThat(describeVpcsResponse.vpcs()).hasSize(1);
    Vpc vpc = describeVpcsResponse.vpcs().get(0);
    assertThat(vpc.isDefault()).isTrue();
  }

  @Given("no EC2 instance")
  public void no_ec2_instance() {
    DescribeInstancesResponse describeInstancesResponse = ec2Client.describeInstances();
    List<Instance> runningInstances = describeInstancesResponse.reservations().stream()
        .flatMap(reservation -> reservation.instances().stream())
        .filter(instance -> Objects.equals(instance.state().name(), InstanceStateName.RUNNING))
        .collect(Collectors.toList());
    assertThat(runningInstances).isEmpty();
  }

  @SneakyThrows
  @When("i create the following EC2 instance in the default VPC")
  public void i_create_the_following_ec2_instance_in_the_default_vpc(io.cucumber.datatable.DataTable dataTable) {
    Map<String, String> params = dataTable.asMaps().get(0);
    String instanceType = params.get("instance_type");
    int instanceCount = Integer.parseInt(params.get("instance_count"));
    String instanceName = String.format("test-ec2-instance-%s", correlationId);

    String args = String.format("-var 'instance_type=%s' -var 'instance_count=%s' -var 'name=%s'", instanceType, instanceCount, instanceName);
    int exitValue = Utils.executeLinuxShellCommand(String.format("terraform apply -auto-approve %s", args), Paths.get(terraformScriptPath));
    log.info("executed with return value {}", exitValue);
  }

  @Then("there is exactly {int} instance with the following attributes")
  public void there_is_exactly_instance_with_the_following_attributes(Integer int1, io.cucumber.datatable.DataTable dataTable) {
    InstanceType expectedInstanceType = InstanceType.fromValue(dataTable.asMaps().get(0).get("instance_type"));
    List<Instance> runningInstances = ec2Client.describeInstances().reservations().stream()
        .flatMap(reservation -> reservation.instances().stream())
        .filter(instance -> Objects.equals(instance.state().name(), InstanceStateName.RUNNING))
        .collect(Collectors.toList());
    assertThat(runningInstances).hasSize(1);
    assertThat(runningInstances.get(0).instanceType()).isEqualTo(expectedInstanceType);
  }
}
