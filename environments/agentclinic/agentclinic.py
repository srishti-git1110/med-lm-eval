from typing import Optional
import verifiers as vf
import requests
import json


class AgentClinicEnv(vf.MultiTurnEnv):
    def __init__(
        eval_dataset,
        max_turns: int = 10,
        parser: Optional[vf.Parser] = None,
        rubric: Optional[vf.Rubric] = None, 
        **kwargs
    ):
        super().__init__(
            eval_dataset=eval_dataset, max_turns=max_turns, parser=parser or vf.Parser(), rubric=rubric, **kwargs
        )


def _get_data(url: str) -> list[dict]:
    data = []
    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue
            example = json.loads(line)
            data.append(example)
    return data


def load_environment(
    dataset_name: str = "agentclinic_medqa_extended.jsonl",
) -> vf.Environment:
    '''
    Loads a custom environment.
    '''
    URL = (
        "https://raw.githubusercontent.com/"
        "SamuelSchmidgall/AgentClinic/"
        "b6570edefb940857a7c334350656b29f9d984f24/"
        f"{dataset_name}"
    )
    data = _get_data(URL)


    



    
