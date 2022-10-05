import argparse as ap
import requests
import os.path
import json


def run_parser():
    parser = ap.ArgumentParser(description="Automatically format TornCity business resume with relevant information.",
                               usage='usage: TRG.py [-o][-c] [-h]'
                               )

    parser.add_argument('-o',
                        dest='owner_name',
                        help='Input for the name of the business owner. usage: -o\"owner_name\"',
                        type=str,
                        required=True
                        )

    parser.add_argument('-c',
                        dest='company_name',
                        help='Input for the name of the business. usage: -c\"company_name\"',
                        type=str,
                        required=True
                        )

    return parser.parse_args()


def gen_query(api_key):
    return f'https://api.torn.com/user/?selections=education,workstats,merits,profile&key={api_key}'


def load_config() -> dict[any: any]:
    with open('config.json', "r") as f:
        return json.load(f)


def load_resume() -> str:
    with open('base_resume.txt', "r") as f:
        return f.read()


def format_skills(skills_data: dict[any: any]) -> str:
    manual_labor = f"{skills_data['manual_labor']:,}"
    intelligence = f"{skills_data['intelligence']:,}"
    endurance = f"{skills_data['endurance']:,}"
    merits_bonus = f"+{skills_data['merits']['Employee Effectiveness']} Employee Effectiveness"
    business_education = f"{len([edu for edu in skills_data['education_completed'] if edu < 14])}/13 Completed"
    return f'Manual Labor: {manual_labor}\n' \
           f'Intelligence: {intelligence}\n' \
           f'Endurance: {endurance}\n' \
           f'Merit: {merits_bonus}\n' \
           f'Business Courses: {business_education}'


def ensure_path(output_path):
    path: str = ''
    for p in output_path.split('/'):
        path += f'{p}/'
        if not os.path.exists(path):
            os.mkdir(path)
    return path


def write_resume(output_path: str, resume_formatted: str, business: str):
    with open(f"{ensure_path(output_path)}{business.replace(' ', '_')}_resume.txt", "w") as f:
        f.write(resume_formatted)


if __name__ == '__main__':
    args = run_parser()
    config = load_config()
    response = requests.get(gen_query(config['api_key'])).json()

    resume = load_resume()

    resume = resume.replace(config['key_words']['__name__'], args.owner_name)
    resume = resume.replace(config['key_words']['__company__'], args.company_name)
    resume = resume.replace(config['key_words']['__skills__'], format_skills(response))
    resume = resume.replace(config['key_words']['__user__'], f"{response['name']}[{response['player_id']}]")

    write_resume(config['output_path'], resume, args.company_name)
