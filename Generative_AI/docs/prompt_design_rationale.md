# Prompt Design Rationale

## 1. Purpose of the Prompt Design Work

The supervised learning model in this project predicts whether a bank customer is likely to churn based on structured features such as credit score, balance, activity level, and number of products. However, the prediction result alone is not sufficient for practical use. A label such as "Likely to Churn" does not directly help a customer, banker, analyst, or marketing team unless it is translated into understandable and useful language.

For this reason, the Generative AI component was designed to act as a communication and decision-support layer on top of the supervised model. Its role is to transform structured customer features and churn predictions into recommendations, explanations, or retention-oriented guidance that match the needs of different target users in the bank customer churn advice system.

The prompt design work was therefore an essential part of Phase 2. The quality of the final generated output depends not only on the language model itself, but also on how the task is framed, how the customer case is represented, and how well the prompt matches the intended use case.

## 2. Prompt Development Strategy

Four prompt templates were developed in this phase, each for a different intended use case:

- customer-facing advice
- banker action recommendation
- analyst explanation
- marketing retention support

Different prompt designs were necessary because these users do not need the same kind of output. A customer needs clear and supportive language. A banker needs concise and action-oriented guidance. An analyst needs explanation and interpretability. A marketing team needs short, structured, and reusable content.

Because of these differences, one generic prompt would not have been sufficient. Instead, the prompts were deliberately varied in tone, detail, structure, and constraints so that the same churn prediction system could support different practical needs without changing the overall project scope.

## 3. Template-by-Template Rationale

### T1 — Customer Retention Advice Template

The target user for this template is the bank customer. Its intended use case is to provide supportive and simple advice after a churn prediction is generated. The purpose is not to explain the model in technical terms, but to offer clear next steps in language that is easy to understand.

This template uses one-shot prompting. This technique was selected because example-guided prompts help the model produce more consistent and readable customer-facing outputs. Since the customer is a non-expert user, the response should be supportive, clear, and non-technical.

Banking domain knowledge influenced this template by shaping the recommendations around realistic actions such as increasing account engagement, reviewing available services, and contacting the bank for guidance. The wording avoids technical machine learning language and avoids making unrealistic financial promises.

### T2 — Banker Action Recommendation Template

The target user for this template is a banker, relationship manager, or retention officer. Its intended use case is to provide a quick internal action recommendation based on the churn prediction result and customer features.

This template uses zero-shot prompting. This technique fits because the banker’s task is direct and operational. The output does not require an example to establish tone. Instead, it requires a professional and structured response that supports immediate action.

Banking domain knowledge shaped this prompt by focusing on practical internal fields such as risk summary, recommended next action, reason for action, and priority level. This reflects how bank staff would typically interpret a churn case in a retention workflow.

### T3 — Banking Analyst Explanation Template

The target user for this template is an analyst, reviewer, or internal reporting user. Its intended use case is to explain likely churn risk using structured evidence from the available customer features.

This template uses reasoning-based prompting. This technique fits because the analyst needs more than a recommendation. The analyst needs interpretability. The output should explain likely churn drivers, identify protective factors, and suggest an appropriate retention focus.

Banking domain knowledge strongly influenced this prompt by including concepts such as engagement level, relationship depth, product usage, protective indicators, and retention focus. This template was designed to make the churn result more interpretable while remaining grounded in the available structured data.

### T4 — Marketing Retention Campaign Template

The target user for this template is a marketing or CRM team. Its intended use case is to provide concise campaign-oriented retention guidance that can support outreach planning.

This template uses constraint-based prompting. This technique fits because marketing-oriented outputs benefit from brevity, consistency, and reusable structure. The goal is not to generate a long explanation, but to produce a short and practical output that can support communication planning.

Banking domain knowledge influenced this template by shaping the output around segment, risk level, message goal, service focus, and outreach channel. These fields are useful in marketing and retention planning, especially when customers need to be grouped into meaningful communication strategies.

## 4. Evolution During Testing

The prompts improved through iterative testing and refinement.

Template T1 improved after adding one-shot example guidance. Early versions were more generic, but the example made the customer-facing style more supportive and consistent.

Template T2 improved after adding a fixed operational structure. Without this structure, the outputs were sometimes too broad. Requiring a risk summary, next action, reason, and priority made the banker-oriented response more useful.

Template T3 improved after requiring clear explanatory sections. This helped the model separate interpretation, churn drivers, protective factors, and retention focus instead of mixing them into one general paragraph.

Template T4 improved after applying format and length constraints. Early outputs were sometimes too broad or too similar to the banker template. The constraints made the output more concise, structured, and aligned with marketing use.

These changes showed that prompt performance improved when the expected output format was stated clearly and matched the real needs of the intended user.

## 5. Lessons Learned

Several lessons were learned during the prompt design process.

First, prompt design should match the intended use case. A prompt that works well for analysts may not work well for customers, because the two users need different levels of detail and different tone.

Second, domain-aware wording improves output relevance. When prompts were written using banking-related concepts such as engagement, service fit, relationship depth, and retention focus, the outputs became more realistic and useful.

Third, structured prompts improve consistency. When the model was given a clear expected format, the outputs became easier to compare across cases and more useful in practice.

Fourth, safe wording helps reduce unsupported claims. Since churn prediction is probabilistic rather than certain, the prompts needed to avoid overconfident language and avoid implying facts that were not provided in the customer data.

Finally, one prompt cannot equally serve all users in the churn advice system. This confirmed the value of designing multiple templates rather than relying on a single generic response style.

## 6. Best Practices Applied

The prompt design process in this project applied several prompt engineering best practices:

- clear task framing
- explicit target user and intended use case
- grounding in provided customer features and prediction output
- controlled tone based on the user’s needs
- structured outputs where appropriate
- realistic wording suitable for a banking setting
- avoidance of unsupported certainty or invented facts

These practices helped improve output quality and made the generated responses more suitable for academic evaluation and practical system integration.

## 7. Final Observation

The strongest overall template was the Banking Analyst Explanation Template. It provided the best balance of interpretability, personalization, and banking-domain relevance. Compared with the other templates, it made the churn prediction more meaningful by linking customer features to likely churn drivers and retention priorities in a structured way.

Although the other templates were useful for their own intended use cases, the analyst template best demonstrated the value of Generative AI in this project because it added explanation, not only output variation. For this reason, it was selected as the strongest overall prompt design for the final system.