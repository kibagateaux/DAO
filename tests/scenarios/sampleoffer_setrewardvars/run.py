from utils import calculate_bytecode

scenario_description = (
    "Test that the DAO can properly set rewardDivisor and "
    "deploymentReward variables"
)


def run(ctx):
    ctx.assert_scenario_ran('proposal')
    reward_divisor = 50000
    deployment_reward = 85200
    set_div_bytecode = calculate_bytecode(
        'setRewardDivisor', ('uint256', reward_divisor)
    )
    set_deploy_bytecode = calculate_bytecode(
        'setDeploymentReward', ('uint256', deployment_reward)
    )
    ctx.create_js_file(substitutions={
        "dao_abi": ctx.dao_abi,
        "dao_address": ctx.dao_addr,
        "offer_abi": ctx.offer_abi,
        "offer_address": ctx.offer_addr,
        "proposal_deposit": ctx.args.proposal_deposit,
        "set_div_bytecode": set_div_bytecode,
        "set_deploy_bytecode": set_deploy_bytecode,
        "debating_period": ctx.args.proposal_debate_seconds,
    })
    print(
        "Notice: Debate period is {} seconds so the test will wait "
        "as much".format(ctx.args.proposal_debate_seconds)
    )

    ctx.execute(expected={
        "offer_reward_divisor": reward_divisor,
        "offer_deployment_reward": deployment_reward
    })
