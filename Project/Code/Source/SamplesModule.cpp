
#include <AzCore/Memory/SystemAllocator.h>
#include <AzCore/Module/Module.h>

#include "SamplesSystemComponent.h"

namespace Samples
{
    class SamplesModule
        : public AZ::Module
    {
    public:
        AZ_RTTI(SamplesModule, "{590484da-b784-4b2a-9442-4f333ef9ad6c}", AZ::Module);
        AZ_CLASS_ALLOCATOR(SamplesModule, AZ::SystemAllocator, 0);

        SamplesModule()
            : AZ::Module()
        {
            // Push results of [MyComponent]::CreateDescriptor() into m_descriptors here.
            m_descriptors.insert(m_descriptors.end(), {
                SamplesSystemComponent::CreateDescriptor(),
            });
        }

        /**
         * Add required SystemComponents to the SystemEntity.
         */
        AZ::ComponentTypeList GetRequiredSystemComponents() const override
        {
            return AZ::ComponentTypeList{
                azrtti_typeid<SamplesSystemComponent>(),
            };
        }
    };
}// namespace Samples

AZ_DECLARE_MODULE_CLASS(Gem_Samples, Samples::SamplesModule)
