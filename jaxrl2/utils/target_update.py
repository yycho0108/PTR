import jax

from jaxrl2.types import Params

from functools import partial

if hasattr(jax, 'tree_multimap'):
    tree_map= jax.tree_multimap
else:
    tree_map= jax.tree_map

def soft_target_update(critic_params: Params, target_critic_params: Params, tau: float) -> Params:
    new_target_params = tree_map(lambda p, tp: p * tau + tp * (1 - tau), critic_params, target_critic_params)
    return new_target_params

@partial(jax.pmap, axis_name='pmap', static_broadcasted_argnums=(2))
def soft_target_update_parallel(critic_params: Params, target_critic_params: Params, tau: float) -> Params:
    new_target_params = tree_map(lambda p, tp: p * tau + tp * (1 - tau), critic_params, target_critic_params)
    return new_target_params
